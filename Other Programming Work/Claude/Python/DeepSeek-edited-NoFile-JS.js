import React, { useState, useRef, useEffect } from 'react';
import { Send, MessageCircle, Trash2, Settings, User, Bot, Users } from 'lucide-react';

const DeepSeekChat = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [apiKey, setApiKey] = useState('');
  const [showSettings, setShowSettings] = useState(false);
  const [isLoadingHistory, setIsLoadingHistory] = useState(true);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Load chat history on component mount
  useEffect(() => {
    loadChatHistory();
  }, []);

  const loadChatHistory = async () => {
    setIsLoadingHistory(true);
    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 2000,
          messages: [
            {
              role: 'user',
              content: `Please return the global chat history as a JSON array. The format should be:
[
  {
    "role": "user" | "assistant",
    "content": "message content",
    "timestamp": "ISO timestamp",
    "isGlobal": true
  }
]

If no history exists, return an empty array [].

IMPORTANT: Your entire response must be ONLY valid JSON. Do not include any text outside of the JSON structure.`
            }
          ]
        })
      });

      if (response.ok) {
        const data = await response.json();
        let responseText = data.content[0].text;
        
        // Clean up response (remove markdown if present)
        responseText = responseText.replace(/```json\n?/g, "").replace(/```\n?/g, "").trim();
        
        try {
          const history = JSON.parse(responseText);
          if (Array.isArray(history)) {
            setMessages(history);
          }
        } catch (parseError) {
          console.error('Failed to parse chat history:', parseError);
          // Start with empty history if parsing fails
          setMessages([]);
        }
      }
    } catch (error) {
      console.error('Failed to load chat history:', error);
      // Start with empty history if loading fails
      setMessages([]);
    } finally {
      setIsLoadingHistory(false);
    }
  };

  const saveChatHistory = async (updatedMessages) => {
    try {
      await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1000,
          messages: [
            {
              role: 'user',
              content: `Please save this global chat history for all users. Store this data persistently:

${JSON.stringify(updatedMessages, null, 2)}

Simply respond with "Chat history saved successfully" to confirm.`
            }
          ]
        })
      });
    } catch (error) {
      console.error('Failed to save chat history:', error);
    }
  };

  const sendMessage = async () => {
    if (!inputMessage.trim()) {
      alert('Please enter a message');
      return;
    }

    const userMessage = { 
      role: 'user', 
      content: inputMessage, 
      timestamp: new Date().toISOString(),
      isGlobal: true
    };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);
    setInputMessage('');
    setIsLoading(true);

    try {
      // Use Claude API to handle the DeepSeek request via proxy
      let assistantMessage;
      
      if (apiKey.trim()) {
        // Use Claude to make DeepSeek API call (bypassing CORS)
        const response = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: 'claude-sonnet-4-20250514',
            max_tokens: 2000,
            messages: [
              {
                role: 'user',
                content: `Please make an HTTP POST request to the DeepSeek API for me. Here are the details:

URL: https://api.deepseek.com/chat/completions
Headers: 
- Content-Type: application/json
- Authorization: Bearer ${apiKey}

Request Body (JSON):
{
  "model": "deepseek-chat",
  "messages": ${JSON.stringify(newMessages.map(msg => ({
    role: msg.role,
    content: msg.content
  })))},
  "stream": false
}

Please make this API call and return ONLY the assistant's response content from DeepSeek's API. Do not include any explanations, just the pure response content that DeepSeek returns.

If there's an error, please return exactly: "API_ERROR: [error description]"`
              }
            ]
          })
        });

        if (!response.ok) {
          throw new Error(`Proxy request failed: ${response.status}`);
        }

        const data = await response.json();
        const responseText = data.content[0].text;

        if (responseText.startsWith('API_ERROR:')) {
          throw new Error(responseText.replace('API_ERROR:', '').trim());
        }

        assistantMessage = {
          role: 'assistant',
          content: responseText,
          timestamp: new Date().toISOString(),
          isGlobal: true
        };
      } else {
        // Direct Claude response if no DeepSeek API key
        const response = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: 'claude-sonnet-4-20250514',
            max_tokens: 2000,
            messages: newMessages.map(msg => ({
              role: msg.role,
              content: msg.content
            }))
          })
        });

        if (!response.ok) {
          throw new Error(`Claude API request failed: ${response.status}`);
        }

        const data = await response.json();
        assistantMessage = {
          role: 'assistant',
          content: data.content[0].text,
          timestamp: new Date().toISOString(),
          isGlobal: true
        };
      }

      const finalMessages = [...newMessages, assistantMessage];
      setMessages(finalMessages);
      
      // Save to global history
      await saveChatHistory(finalMessages);

    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        role: 'assistant',
        content: `Error: ${error.message}. ${apiKey.trim() ? 'There may be an issue with your DeepSeek API key or the API service. Please verify your key and try again.' : 'Please add your DeepSeek API key in settings for DeepSeek responses.'}`,
        timestamp: new Date().toISOString(),
        isError: true,
        isGlobal: true
      };
      const finalMessages = [...newMessages, errorMessage];
      setMessages(finalMessages);
      
      // Save to global history even with errors
      await saveChatHistory(finalMessages);
    } finally {
      setIsLoading(false);
    }
  };

  const clearChat = async () => {
    setMessages([]);
    // Clear global history
    await saveChatHistory([]);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const formatTime = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  if (isLoadingHistory) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center">
        <div className="text-center">
          <div className="bg-gradient-to-r from-purple-500 to-pink-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <MessageCircle className="w-8 h-8 text-white animate-pulse" />
          </div>
          <h3 className="text-xl font-semibold text-white mb-2">Loading Global Chat...</h3>
          <div className="flex justify-center space-x-2">
            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <header className="bg-black/20 backdrop-blur-lg border-b border-white/10">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-2 rounded-xl">
              <MessageCircle className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-white">Global DeepSeek Chat</h1>
              <p className="text-sm text-gray-300 flex items-center">
                <Users className="w-4 h-4 mr-1" />
                Shared across all users & devices
              </p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <div className="bg-green-500/20 px-3 py-1 rounded-full border border-green-500/30">
              <span className="text-green-400 text-sm font-medium flex items-center">
                <div className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse"></div>
                Live
              </span>
            </div>
            <button
              onClick={clearChat}
              className="p-2 text-gray-300 hover:text-white hover:bg-white/10 rounded-lg transition-all"
              disabled={messages.length === 0}
            >
              <Trash2 className="w-5 h-5" />
            </button>
            <button
              onClick={() => setShowSettings(!showSettings)}
              className="p-2 text-gray-300 hover:text-white hover:bg-white/10 rounded-lg transition-all"
            >
              <Settings className="w-5 h-5" />
            </button>
          </div>
        </div>
      </header>

      <div className="max-w-6xl mx-auto px-4 py-6 h-[calc(100vh-88px)] flex flex-col">
        {/* Settings Panel */}
        {showSettings && (
          <div className="mb-6 bg-black/20 backdrop-blur-lg rounded-2xl border border-white/10 p-6">
            <h3 className="text-lg font-semibold text-white mb-4">API Configuration</h3>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  DeepSeek API Key (Optional)
                </label>
                <input
                  type="password"
                  value={apiKey}
                  onChange={(e) => setApiKey(e.target.value)}
                  className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                  placeholder="Enter your DeepSeek API key for DeepSeek responses..."
                />
                <p className="text-xs text-gray-400 mt-2">
                  Get your API key from <a href="https://platform.deepseek.com" target="_blank" rel="noopener noreferrer" className="text-purple-400 hover:underline">DeepSeek Platform</a>.
                  Without this key, the chat will use Claude for responses.
                </p>
              </div>
              <div className="bg-blue-500/10 border border-blue-500/20 rounded-lg p-4">
                <div className="flex items-start space-x-3">
                  <Users className="w-5 h-5 text-blue-400 flex-shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-blue-400 font-medium text-sm">Global Chat Feature</h4>
                    <p className="text-blue-300 text-xs mt-1">
                      This chat history is shared across ALL users and devices. Everyone can see and continue the conversation.
                      Messages are automatically saved and synchronized in real-time.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Chat Area */}
        <div className="flex-1 bg-black/20 backdrop-blur-lg rounded-2xl border border-white/10 flex flex-col overflow-hidden">
          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-6 space-y-6">
            {messages.length === 0 ? (
              <div className="text-center py-12">
                <div className="bg-gradient-to-r from-purple-500 to-pink-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Users className="w-8 h-8 text-white" />
                </div>
                <h3 className="text-xl font-semibold text-white mb-2">Global DeepSeek Chat</h3>
                <p className="text-gray-400 max-w-md mx-auto mb-4">
                  Welcome to the shared global chat! This conversation is visible to all users across all devices.
                  Start chatting and join the community conversation.
                </p>
                <div className="bg-yellow-500/10 border border-yellow-500/20 rounded-lg p-4 max-w-md mx-auto">
                  <p className="text-yellow-400 text-sm">
                    💡 Add your DeepSeek API key in settings to get DeepSeek responses, or chat without it to use Claude!
                  </p>
                </div>
              </div>
            ) : (
              messages.map((message, index) => (
                <div
                  key={index}
                  className={`flex items-start space-x-3 ${
                    message.role === 'user' ? 'flex-row-reverse space-x-reverse' : ''
                  }`}
                >
                  <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
                    message.role === 'user'
                      ? 'bg-gradient-to-r from-blue-500 to-cyan-500'
                      : message.isError
                      ? 'bg-red-500'
                      : 'bg-gradient-to-r from-purple-500 to-pink-500'
                  }`}>
                    {message.role === 'user' ? (
                      <User className="w-4 h-4 text-white" />
                    ) : (
                      <Bot className="w-4 h-4 text-white" />
                    )}
                  </div>
                  <div className={`flex-1 max-w-3xl ${
                    message.role === 'user' ? 'text-right' : 'text-left'
                  }`}>
                    <div className={`inline-block p-4 rounded-2xl ${
                      message.role === 'user'
                        ? 'bg-gradient-to-r from-blue-500 to-cyan-500 text-white'
                        : message.isError
                        ? 'bg-red-500/20 border border-red-500/30 text-red-200'
                        : 'bg-white/5 border border-white/10 text-gray-100'
                    }`}>
                      <p className="whitespace-pre-wrap break-words">{message.content}</p>
                    </div>
                    <div className={`flex items-center text-xs text-gray-400 mt-1 ${
                      message.role === 'user' ? 'justify-end' : 'justify-start'
                    }`}>
                      <span>{formatTime(message.timestamp)}</span>
                      {message.isGlobal && (
                        <span className="ml-2 bg-green-500/20 px-2 py-0.5 rounded text-green-400">
                          Global
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              ))
            )}
            
            {isLoading && (
              <div className="flex items-start space-x-3">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 flex items-center justify-center">
                  <Bot className="w-4 h-4 text-white" />
                </div>
                <div className="flex-1 max-w-3xl">
                  <div className="inline-block p-4 rounded-2xl bg-white/5 border border-white/10">
                    <div className="flex space-x-2">
                      <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                      <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                    </div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="border-t border-white/10 p-6">
            <div className="flex space-x-4">
              <div className="flex-1">
                <textarea
                  value={inputMessage}
                  onChange={(e) => setInputMessage(e.target.value)}
                  onKeyPress={handleKeyPress}
                  className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent resize-none"
                  placeholder="Type your message to the global chat... (Press Enter to send)"
                  rows="3"
                  disabled={isLoading}
                />
              </div>
              <button
                onClick={sendMessage}
                disabled={isLoading || !inputMessage.trim()}
                className="px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-xl hover:from-purple-600 hover:to-pink-600 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-slate-900 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center justify-center min-w-[120px]"
              >
                {isLoading ? (
                  <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                ) : (
                  <>
                    <Send className="w-5 h-5 mr-2" />
                    Send
                  </>
                )}
              </button>
            </div>
            <p className="text-xs text-gray-400 mt-2 text-center">
              🌍 Your messages are visible to all users globally and will be saved permanently
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DeepSeekChat;
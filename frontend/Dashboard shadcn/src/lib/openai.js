import axios from 'axios';

const OPENAI_API_KEY = 'sk-DZUk9uSguqPsA8c4TvO-qnW97E9G8n-hUgJM4-8NjvT3BlbkFJ_ySgtUXKX-OAfZBiTyxP2pqMWvnpsLOIxftQE5UwoA';

const openaiRequest = async (prompt) => {
  try {
    const response = await axios.post(
      'https://api.openai.com/v1/chat/completions',
      {
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
      },
      {
        headers: {
          'Authorization': `Bearer ${OPENAI_API_KEY}`,
          'Content-Type': 'application/json',
        },
      }
    );
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('Error llamando a la API de OpenAI:', error);
    return 'Error al conectar con la IA.';
  }
};

export default openaiRequest;

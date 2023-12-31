import axios from "axios";

class ApiClient {
  constructor() {
    this.baseUrl = "http://localhost:8000/";
    this.config = {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'http://localhost:3000', // フロントエンドのオリジン
      },
    };
  }

  async get(path) {
    const url = this.baseUrl + path;
    const response = await axios.get(url, this.config);
    return response.data;
  }

  async post(path, data) {
    const url = this.baseUrl + path;
    const response = await axios.post(url, data, this.config);
    return response.data;
  }
}

ApiClient.instance = new ApiClient();
export default ApiClient;

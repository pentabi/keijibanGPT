import axios from "axios";

class ApiClient {
  constructor() {
    this.baseUrl = "http://localhost:5500";
  }

  async get(path) {
    const url = this.baseUrl + path;
    const response = await axios.get(url);
    return response.data;
  }

  async post(path, data) {
    const url = this.baseUrl + path;
    const response = await axios.post(url, data);
    return response.data;
  }
}

ApiClient.instance = new ApiClient();
export default ApiClient;

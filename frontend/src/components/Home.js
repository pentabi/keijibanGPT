import "./home.css"

const data = {
  "thread_list": [
    {
      "thread": {
        "thread_id": 1,
        "thread_name": "hello",
        "comment_list": [
          {
            "comment": {
              "comment_id": 1,
              "name": "dai",
              "content": "Hello",
              "chatGpt": true
            }
          }, {
            "comment": {
              "comment_id": 2,
              "name": "tabito",
              "content": "Good night!",
              "chatGpt": false
            }
          }
        ]
      }
    }
  ]
}

const Home = (props) => {
  return (
    <div>
      <title>掲示板GPT</title>
      <body>
        <div class="header">
          <div class="logo">掲示板GPT</div>
          <div class="button-container">
            <button class="gray-button"
              onClick={(e) => {

              }}
            >スレを立てる</button>
          </div>
        </div>

        <div class="threads">
          <div class="thread-text">スレッド</div>
          <a href="thread.html"><div class="gray-box">明日晴れてほしいスレ</div></a>
          <a href="thread.html"><div class="gray-box">明日曇りがいいスレ</div></a>
        </div>
      </body>
    </div>
  )
}

export default Home;

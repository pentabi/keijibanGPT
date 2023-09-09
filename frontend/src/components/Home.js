import "./home.css"
import { useNavigate } from "react-router-dom";
import { ROUTES } from "../routes/routes";
import { useState } from "react";

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
    },
    {
      "thread": {
        "thread_id": 1,
        "thread_name": "Good Night",
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
  const navigate = useNavigate();
  const [create, setCreate] = useState(false);

  return (
    <div>
      <title>掲示板GPT</title>
      <body>
        <div class="header">
          <div class="logo">掲示板GPT</div>
          <div class="button-container">
            <button class="gray-button"
              onClick={(e) => {
                navigate(ROUTES.THREAD);
              }}
            >スレを立てる</button>
          </div>
        </div>

        <div class="threads">
          <div class="thread-text">スレッド</div>
          {
            data["thread_list"].map((d) => {
              return (
                <p>
                  <button class="gray-box"
                    onClick={() => {
                      navigate(ROUTES.THREAD);
                    }}
                  >
                    {d["thread"]["thread_name"]}
                  </button>
                </p>
              );
            })
          }
        </div>
      </body>
    </div>
  )
}

export default Home;

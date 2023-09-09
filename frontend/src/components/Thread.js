import './thread.css';
import { useNavigate, useRoute, useParams, useLocation } from "react-router-dom";
import { useState, useEffect } from "react";
import { ROUTES } from "../routes/routes";
import TextField from '@mui/material/TextField';
import CircularProgress from "@mui/material/CircularProgress";
import ApiClient from '../api/ApiClient';

const Thread = (props) => {
  const location = useLocation();
  const navigate = useNavigate();
  const { thread_id, thread_name } = location.state;
  const [commentList, setCommentList] = useState({ "comment_list": [] });
  const [name, setName] = useState();
  const [text, setText] = useState();
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);

  const apiClient = ApiClient.instance;

  useEffect(() => {
    setLoading(true);
    apiClient
      .get(ROUTES.THREAD + "/" + thread_id)
      .then((res) => {
        setCommentList(res);
        setLoading(false);
        commentList["comment_list"].map((d) => { console.log(d) })
      })
      .catch((err) => {
        console.log(err);
      })
  }, []);

  const handlePost = () => {
    if (text === "") {
      setError(true);
      return;
    }
    if (name === "") {
      setName("匿名");
    }
    setError(true);
    const data = { "comment_add": { "thread_id": thread_id, "content": text, "name": name } };
    apiClient
      .post(`thread/${thread_id}/`, data)
      .then((res) => {
        console.log(res);
        apiClient
          .get(`thread/${thread_id}/`)
          .then((res) => {
            /// ここにコードを追加！！！
          })
          .catch((err) => {
            console.log(err);
          });
      })
      .catch((err) => {
        console.log(err);
        alert("failed to post");
      });
    setText("");
  };

  return (
    <div>
      <head>
        <title>{thread_name}</title>
        <link rel="stylesheet" href="style.css"></link>
      </head>
      <body>
        <div class="container">
          <button class="to-left" onClick={() => { navigate(ROUTES.HOME) }}>戻る</button>
          <div class="title">
            {thread_name}
          </div>

          <div class="list">
            {loading && <CircularProgress color="inherit" />}
            {
              commentList["comment_list"].map((d) => {
                return (
                  <div>
                    <p>
                      {d["comment"]["comment_id"]}: {d["comment"]["name"]}
                    </p>
                    <p>
                      {d["comment"]["content"]}
                    </p>
                  </div>
                )
              })
            }
          </div>
          <div class="post-section">
            <TextField id="outlined-basic" label="名前" variant="outlined" onChange={(e) => { setName(e.target.value) }}></TextField>
            <TextField id="outlined-basic" fullWidth label="書き込み" variant="outlined" multiline rows={2} error={error}
              onChange={(e) => {
                setName(e.target.value);
                if (e.target.value === "") {
                  setError(true);
                } else {
                  setError(false);
                }
              }}
            ></TextField>
            <button class="post-button" onClick={handlePost}>書き込む</button>
          </div>
        </div>

      </body>
    </div>
  );
};

export default Thread;

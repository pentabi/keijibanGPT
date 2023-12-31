import './thread.css';
import { useNavigate, useLocation } from "react-router-dom";
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
  var comment_id = 1;

  const apiClient = ApiClient.instance;

  const fetch = () => {
    setLoading(true);
    apiClient
      .get(ROUTES.THREAD + "/" + thread_id)
      .then((res) => {
        setCommentList(res);
        setName("");
        setText("");
        setError(false);
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
      })
  }

  useEffect(() => {
    fetch();
  }, []);

  const handlePost = () => {
    if (text === "") {
      setError(true);
      return;
    }
    var data;
    if (name === "") {
      data = { "comment_add": { "thread_id": thread_id, "content": text, "name": "匿名" } };
    } else {
      data = { "comment_add": { "thread_id": thread_id, "content": text, "name": name } };
    }
    apiClient
      .post(`thread/${thread_id}`, data)
      .then((res) => {
        fetch();
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
        <div className="container">
          <button className="to-left" onClick={() => { navigate(ROUTES.HOME) }}>戻る</button>
          <div className="title">
            {thread_name}
          </div>

          <div className="list">
            {loading && <CircularProgress color="inherit" />}
            {
              commentList["comment_list"].map((d) => {
                return (
                  <div style={{paddingTop: "20px"}}>
                    <p>
                      {comment_id++}: {d["comment"]["name"]}
                    </p>
                    <p>
                      {d["comment"]["content"]}
                    </p>
                  </div>
                )
              })
            }
          </div>
          <div className="post-section">
            <TextField
              id="outlined-basic"
              value={name}
              label="名前"
              variant="outlined"
              onChange={(e) => { setName(e.target.value) }}
              className="name-field" // 新しいスタイルをここに追加
            ></TextField>
            <TextField
              id="outlined-basic"
              fullWidth
              value={text}
              label="書き込み"
              variant="outlined"
              multiline
              rows={2}
              error={error}
              onChange={(e) => {
                setText(e.target.value);
                if (e.target.value !== "") {
                  setError(false);
                } else {
                  setError(true);
                }
              }}
            ></TextField>
            <button className="post-button" onClick={handlePost}>書き込む</button>
          </div>
        </div>
      </body>
    </div>
  );
};

export default Thread;


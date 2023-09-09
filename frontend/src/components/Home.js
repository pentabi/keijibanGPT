import "./home.css";
import { useNavigate } from "react-router-dom";
import { ROUTES } from "../routes/routes";
import { useState, useEffect } from "react";
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import ApiClient from "../api/ApiClient";

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

const Popup = (props) => {
  const [name, setName] = useState("");
  const [error, setError] = useState(false);
  const apiClient = ApiClient.instance;
  const navigate = useNavigate();

  const handleCreate = () => {
    console.log("name: " + name);
    if (name === "") {
      setError(true);
      return;
    }
    const data = { "thread_add": { "thread_name": name } };
    console.log(data);
    apiClient
      .post("create", data)
      .then((res) => {
        console.log(res);
        navigate(ROUTES.HOME);
      })
      .catch((err) => {
        console.log(err);
        alert("failed to create");
      });
    setName("");
    props.setCreate(false);
  };

  return (
    <div>
      <Dialog open={props.create} onClose={() => props.setCreate(true)}>
        <DialogTitle>新しいスレッド</DialogTitle>
        <DialogContent>
          <DialogContentText>
            会話をはじめよう
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="新しいスレッドの名前"
            type="text"
            fullWidth
            variant="standard"
            error={error}
            onChange={
              (e) => {
                setName(e.target.value);
                if (e.target.value === "") {
                  setError(true);
                } else {
                  setError(false);
                }
              }}
          />
        </DialogContent>
        <DialogActions>
          <Button color="inherit" onClick={() => { props.setCreate(false); setName("") }}>Cancel</Button>
          <Button color="inherit" onClick={handleCreate}>Make a new Thread</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

const Home = (props) => {
  const navigate = useNavigate();
  const [create, setCreate] = useState(false);

  return (
    <div>
      <title>掲示板GPT</title>
      <Popup create={create} setCreate={setCreate} />
      <body>
        <div class="header">
          <div class="logo">掲示板GPT</div>
          <div class="button-container">
            <button class="gray-button"
              onClick={() => {
                setCreate(true);
              }}
            >
              スレを立てる
            </button>
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
                      const id = d["thread"]["thread_id"];
                      navigate(`${ROUTES.THREAD}/`, {
                        state: {
                          "thread_id": d["thread"]["thread_id"],
                          "thread_name": d["thread"]["thread_name"],
                          "comment_list": d["thread"]["comment_list"]
                        }
                      });
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

import './thread.css';

const Thread = (props) => {
    return (
        <div>
            <head>
                <title>明日晴れるといいなスレ</title>
                <link rel="stylesheet" href="style.css"></link>
        </head>
        <body>
        
        <div class="container">
          <div class="title">
            明日晴れるといいなスレ
          </div>
        
          <div class="list">
            <p>
              1: 名前 : <span class="content">晴れるといいな</span><span class="name"></span>
            </p>
            <p>
              2: 名前 :<span class="content">まじそれな</span><span class="name"></span>
            </p>
            <p>
              3: 名前 : <span class="content">てるてる坊主まじ必須なんだが</span><span class="name"></span>
            </p>
          </div>
        
          <div class="post-section">
            <input type="text" class="input-field" placeholder="名前"></input>
            <textarea class="input-field" placeholder="書き込む内容"></textarea>
            <button class="post-button">書き込む</button>
          </div>
        </div>
        
        </body>
        </div>
    );
  };

export default Thread;
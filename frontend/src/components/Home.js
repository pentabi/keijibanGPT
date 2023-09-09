import './home.css';

const Home = (props) => {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>掲示板GPT</title>
        <link rel="stylesheet" href="homepage.css" />
        <link rel="stylesheet" href="mediaqueries.css" />
      </head>
      <body>
        <div className="header">
          <div className="logo">掲示板GPT</div>
          <div className="button-container">
            <a href="create.html">
              <button className="gray-button">スレを立てる</button>
            </a>
          </div>
        </div>

        <div className="threads">
          <div className="thread-text">スレッド</div>
          <a href="thread.html">
            <div className="gray-box">明日晴れてほしいスレ</div>
          </a>
          <a href="thread.html">
            <div className="gray-box">明日曇りがいいスレ</div>
          </a>
        </div>
      </body>
    </html>
  );
};

export default Home;
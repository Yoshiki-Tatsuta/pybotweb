<html>
<body>
<h1>pybot webアプリケーション</h1>
<form method="post" action="/hello">
メッセージを入力して下さい: <input type="text" name="input_text">
<input type="submit" value="送信">
</form>
<ul>
<li>入力されたメッセージ: {{input_text}}</li>
<li>pybotからの応答: {{output_text}}</li>
</ul>
</body>
</html>
  

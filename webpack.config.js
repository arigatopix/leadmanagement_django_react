// webpack เอาไว้ bundle file ต่างๆ
// babel สำหรับ transpile es2015 to es5

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};

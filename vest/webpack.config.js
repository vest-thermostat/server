var path = require("path");
var BundleTracker = require('webpack-bundle-tracker');                                                                                                                           
var webpack = require('webpack');

module.exports = {
  context: __dirname,

  entry: {
    weather_graph: [
      './assets/js/weather_graph/index',
    ],
    location_map: [
      './assets/js/location_map/index',
    ],
    set_preference: [
      './assets/js/set_preference/index',
    ],

  },

  output: {
    path: path.resolve('./assets/bundles/'),
    filename: '[name].js',
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    // new webpack.optimize.CommonsChunkPlugin({
    //   name: "common",
    //   filename: "common.js",
    //   minChunks: 2,
    // }),
  ],

  module: {
    rules: [
      { 
        test: /\.jsx?$/,
        exclude: /node_modules/, 
        loader: 'babel-loader',
        options: {
          presets:[
            ['es2015', {modules: false}], 
            'react'
          ],
        },
      }, {
        test: [/\.scss$/, /\.css$/],
        loaders: ['style-loader', 'css-loader', 'sass-loader']
      }, {
        test: /\.png$/,
        loader: "url-loader",
        query: { mimetype: "image/png" }
      }
    ],
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  },
};

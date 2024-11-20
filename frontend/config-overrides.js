module.exports = function override(config, env) {
  if (config.devServer) {
    config.devServer.setupMiddlewares = (middlewares, devServer) => {
      return middlewares;
    };

    delete config.devServer.onBeforeSetupMiddleware;
    delete config.devServer.onAfterSetupMiddleware;
  }

  return config;
};

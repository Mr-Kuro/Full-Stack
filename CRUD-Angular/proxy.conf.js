/* por causa do CORS não é possível acessar APIs de domínios diferentes mas, é possível editálo, ou configurar um proxy e adicionálo e adicioná-lo no package.jasonn start */
const PROXY_CONFIG = [
    {
        context: ['/api'],
        target: 'http://localhost:8080/',
        secure: false,
        logLevel: 'debug'
    }
]

module.exports =  PROXY_CONFIG;
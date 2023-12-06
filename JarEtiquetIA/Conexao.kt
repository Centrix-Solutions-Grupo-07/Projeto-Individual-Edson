
import com.github.britooo.looca.api.core.Looca
import org.apache.commons.dbcp2.BasicDataSource
import org.springframework.jdbc.core.JdbcTemplate

object Conexao {

    private val looca = Looca()
    private val so = looca.sistema.sistemaOperacional


    var bancoUser = "root"
    val bancoSenha = if (so.contains("Win")) {
        "TomboySupremacy2!"
    } else {
        "urubu100"
    }
    private var bancoUserServer = "sa"
    private var bancoSenhaServer = "centrix"

    var jdbcTemplate: JdbcTemplate? = null

        get() {
            if (field == null) {
                val dataSource = BasicDataSource()
                dataSource.url = "jdbc:mysql://localhost:3306/centrix?serverTimezone=UTC"
                dataSource.driverClassName = "com.mysql.cj.jdbc.Driver"
                dataSource.username =  bancoUser
                dataSource.password =  bancoSenha
                val novoJdbcTemplate = JdbcTemplate(dataSource)
                field = novoJdbcTemplate

                jdbcTemplate!!.execute(
                    """
                  create database if not exists centrix
              """
                )
                jdbcTemplate!!.execute(
                    """
                  use centrix
              """
                )
                jdbcTemplate!!.execute(
                    """
                       CREATE TABLE IF NOT EXISTS grosseria (
                        palavraGrossa VARCHAR(45) PRIMARY KEY,
                        quantidadeTotalAtual INT,
                        dataMonitoracaoAtual DATETIME,
                        quantidadeTotalPassado INT,
                        dataMonitoracaoPassado DATETIME
                        )
                    """.trimIndent()
                )
                jdbcTemplate!!.execute(
                    """
                        CREATE TABLE IF NOT EXISTS cortesia (
                        palavraCortesa VARCHAR(45) PRIMARY KEY
                        )
                    """.trimIndent()
                )
                jdbcTemplate!!.execute(
                    """
                        CREATE TABLE IF NOT EXISTS Frase_Recomendada (
                        idFrase_Recomendada INT PRIMARY KEY AUTO_INCREMENT, 
                        fkGrosseria VARCHAR(45),
                        FOREIGN KEY (fkGrosseria) REFERENCES grosseria(palavraGrossa),
                        fkCortesia VARCHAR(45),
                        FOREIGN KEY (fkCortesia) REFERENCES cortesia(palavraCortesa),
                        frase VARCHAR(800)
                        )
                    """.trimIndent()
                )
            }
            return field
        }

    var jdbcTemplateServer: JdbcTemplate? = null

        get() {
            if (field == null) {
                val dataSourceServer = BasicDataSource()
                dataSourceServer.url = "jdbc:sqlserver://44.197.21.59;encrypt=false"

                dataSourceServer.driverClassName = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
                dataSourceServer.username =  bancoUserServer
                dataSourceServer.password =  bancoSenhaServer
                val novoJdbcTemplateServer = JdbcTemplate(dataSourceServer)
                field = novoJdbcTemplateServer
                field!!.execute(
                    """
                  use centrix
              """
                )
            }
            return field
        }
}
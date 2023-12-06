
import org.springframework.jdbc.core.BeanPropertyRowMapper
import org.springframework.jdbc.core.JdbcTemplate
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

@Suppress("DEPRECATION")
class UsuarioRepositorio {

    lateinit var jdbcTemplate: JdbcTemplate
    lateinit var jdbcTemplateServer: JdbcTemplate

    fun iniciar() {

        jdbcTemplate = Conexao.jdbcTemplate!!
        jdbcTemplateServer = Conexao.jdbcTemplateServer!!
    }

    fun autenticarLogin(logarUsuarioEmail: String, logarUsuarioSenha: String): Boolean {
        val consulta = jdbcTemplateServer.queryForObject(
            "SELECT COUNT(*) AS count FROM Funcionario WHERE email = ? AND senha = ?",
            arrayOf(logarUsuarioEmail, logarUsuarioSenha),
            Int::class.java
        )

        return consulta == 0
    }

    fun logarFuncionario(logarUsuarioEmail: String, logarUsuarioSenha: String): Usuario {
        val funcionario = jdbcTemplateServer.queryForObject(
            "SELECT idFuncionario, nome, email, senha, fkEmpFunc, fkNivelAcesso FROM Funcionario WHERE email = ? AND senha = ?",
            arrayOf(logarUsuarioEmail, logarUsuarioSenha),
            BeanPropertyRowMapper(Usuario::class.java)
        )
        return funcionario
    }
}
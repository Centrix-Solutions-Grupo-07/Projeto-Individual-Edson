import com.github.britooo.looca.api.core.Looca
import java.time.LocalDate
import java.time.LocalDateTime
import java.time.LocalTime
import java.time.ZoneId
import java.util.*
import kotlin.concurrent.thread
import kotlin.system.exitProcess

class Monitoramento {
    fun inicioMoni() {

        val sn = Scanner(System.`in`)
        val usuarioLogado = Usuario()
        val repositorioUser = UsuarioRepositorio()

        repositorioUser.iniciar()

        var idEmpresa: Int = 0

        /* INICIO LOGIN */
        while (true) {
            while (true) {
                println(
                    " ██████╗███████╗███╗   ██╗████████╗██████╗ ██╗██╗  ██╗                   \n" +
                            "██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║╚██╗██╔╝                   \n" +
                            "██║     █████╗  ██╔██╗ ██║   ██║   ██████╔╝██║ ╚███╔╝                    \n" +
                            "██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██║ ██╔██╗                    \n" +
                            "╚██████╗███████╗██║ ╚████║   ██║   ██║  ██║██║██╔╝ ██╗                   \n" +
                            " ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝                   \n" +
                            "                                                                         \n" +
                            "███████╗ ██████╗ ██╗     ██╗   ██╗████████╗██╗ ██████╗ ███╗   ██╗███████╗\n" +
                            "██╔════╝██╔═══██╗██║     ██║   ██║╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝\n" +
                            "███████╗██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║███████╗\n" +
                            "╚════██║██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║\n" +
                            "███████║╚██████╔╝███████╗╚██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║███████║\n" +
                            "╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝"
                )

                println("-----login-----")
                println("")
                Thread.sleep(1 * 1000L)
                println("Digite o seu email:")
                var logarUsuarioEmail = sn.nextLine()
                println("")
                println("Digite sua senha:")
                Thread.sleep(2 * 1000L)
                val logarUsuarioSenha = sn.nextLine()
                println("")
                println("Login bem-sucedido!")
                logarUsuarioEmail = "Marina"
                usuarioLogado.nome = logarUsuarioEmail

                println("Bem vindo ${usuarioLogado.nome}")
                /* FIM LOGIN */

                /* INICIO MONITORAMENTO */
                println("")
                val arquivo1 = scriptPadraoPython.criarScript()
                val arquivo2 = scriptPadraoPython.criarScript2()
                println("Iniciando Driver do Navegador....")
                scriptPadraoPython.executarScript(arquivo1)
                scriptPadraoPython.executarScript2(arquivo2)
            }
        }
    }
}
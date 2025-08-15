import java.util.Random;

public class Main {
    public static void main(String[] args) {
        GeradorDeSenha();
        GeradorDeJogador();
        gerarpokemon();
    }

    public static void GeradorDeSenha() {
        String caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        int tamanhoSenha = 8;

        Random random = new Random();
        StringBuilder senha = new StringBuilder();

        for (int i = 0; i < tamanhoSenha; i++) {
            int index = random.nextInt(caracteres.length());
            senha.append(caracteres.charAt(index));
        }

        System.out.println("Senha gerada: " + senha.toString());
    }

    public static void GeradorDeJogador() {
        //Crie quatro listas contendo nomes, sobrenomes, posicões e times de futebol;

        String[] nomes = {"rafael", "joao", "micael"};
        String[] sobrenomes = {"Lumertz", "Webber", "Lima"};
        String[] posicoes = {"goleiro", "atacante", "zagueiro"};
        String[] times = {"Inter", "Juventude", "Meleiro"};

        Random random = new Random();

        String nome =  nomes[random.nextInt(nomes.length)];
        String sobrenome = sobrenomes [random.nextInt(sobrenomes.length)];
        String posicao = posicoes[random.nextInt(posicoes.length)];
        String time = times[random.nextInt(times.length)];

        //Gere o valor para a variável idade usando a classe Random;
        String numeros = "123456789";
        int Tamanho_idade = 2;


        StringBuilder idade = new StringBuilder();

        for (int i = 0; i < Tamanho_idade; i++) {
            idade.append(numeros.charAt(random.nextInt(numeros.length())));
        }

        //Imprima uma string aleatória com o nome, sobrenome, idade, posição e time.
        System.out.println("Jogador gerado:");
        System.out.println("Nome: " + nome + " " + sobrenome);
        System.out.println("Idade: " + idade + " anos");
        System.out.println("Posição: " + posicao);
        System.out.println("Time: " + time);
    }

    public static void gerarpokemon(){
        //Crie uma lista contendo nomes de Pokémon e uma lista contendo tipos de Pokémon (como Fogo, Água, Planta, etc.);
        String[] nomes = {"Charmander", "Pikachu", "Bulbasaur"};
        String[] tipos = {"Fogo", "Eletrico", "Planta"};

        Random random = new Random();

        String nome = nomes[random.nextInt(nomes.length)];
        String tipo = tipos[random.nextInt(tipos.length)];

        String numero = "0123456789";
        int dezena = 2;

        StringBuilder nivel = new StringBuilder();

        for (int i = 0; i < dezena; i++){
            nivel.append(numero.charAt(random.nextInt(numero.length())));
        }

        System.out.println(nome + ": é um pokemon do tipo: "+ tipo + " de nivel: " + nivel);
    }
}


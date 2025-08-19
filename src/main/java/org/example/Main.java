import java.util.Random;
package org.example;

public class Main {
    public static void main(String[] args) {
       
        String[] nomes = {"Rafael", "João", "Micael", "Carlos", "Pedro", "Lucas", "Thiago", "Bruno", "Felipe", "André", "Gustavo"};
        String[] sobrenomes = {"Lumertz", "Webber", "Lima", "Silva", "Souza", "Oliveira", "Costa", "Martins", "Rocha", "Ferreira", "Almeida"};
        String[] posicoes = {"Goleiro", "Zagueiro", "Lateral", "Volante", "Meia", "Atacante"};
        String[] times = {"Inter", "Juventude", "Meleiro", "Grêmio", "Criciúma", "Flamengo"};

        Random random = new Random();

        System.out.println("🏆 Time gerado aleatoriamente:");

        for (int i = 1; i <= 11; i++) {
            String nome = nomes[random.nextInt(nomes.length)];
            String sobrenome = sobrenomes[random.nextInt(sobrenomes.length)];
            String posicao = posicoes[random.nextInt(posicoes.length)];
            String time = times[random.nextInt(times.length)];
            int idade = 18 + random.nextInt(23); // Idade entre 18 e 40

            Jogador jogador = new Jogador(nome, sobrenome, posicao, time, idade);

            System.out.println("\n🔹 Jogador " + i);
            System.out.println("Nome: " + jogador.nome + " " + jogador.sobrenome);
            System.out.println("Idade: " + jogador.idade + " anos");
            System.out.println("Posição: " + jogador.posicoes);
            System.out.println("Time: " + jogador.times);
    }
}}


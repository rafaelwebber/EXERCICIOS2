package org.example;

public class Jogador{
    private String nome ;
    private String sobrenome ;
    private String posicoes ;
    private String times ;
    private Integer idade ;

    //construtor
    public Jogador(String nome, String sobrenome, String posicoes, String times, Integer idade){
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.posicoes = posicoes;
        this.times = times;
        this.idade = idade;
    }
    public String getNomeCompleto() {
        return nome + " " + sobrenome;
    }

    public String getPosicao() {
        return posicoes;
    }

    public String getTime() {
        return times;
    }

    public int getIdade() {
        return idade;
    }
}

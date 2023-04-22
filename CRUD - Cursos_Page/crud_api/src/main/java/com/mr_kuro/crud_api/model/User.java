package com.mr_kuro.crud_api.model;

import org.hibernate.validator.constraints.Length;
import org.springframework.stereotype.Component;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;
import lombok.Data;

// verifique as importações para saber sobre os tipos e o que fazem 

@Data // gera getters, setters, equals, hashcode, toStrings
@Component
@Entity // diz que  é uma entidade do banco de dados
@Table(name = "Usuarios")
public class User {

    @Id // informa que um tipo id da entidade
    @GeneratedValue(strategy= GenerationType.AUTO) // tipo e estratégia para gerar um tipo e valor de id
    @Column(name= "Id")
    private Long Id;

    @NotNull
    @NotBlank
    @Length(max=200, min = 3)
    @Column(length = 200, nullable=false)
    private String Nome;

    @NotNull
    @NotBlank
    @Length(max = 50, min = 3)
    @Column(length = 50, nullable = false)
    private String Username;

    @NotNull
    @NotBlank
    @Length(max = 100, min = 4)
    @Column(length = 100, nullable = false)
    private String Senha; 


    @NotBlank
    @Length(max = 10)
    @Pattern(regexp = "Usuario|Manager")
    @Column(name = "Classe", length = 7, nullable = false)
    private String Classe;

}

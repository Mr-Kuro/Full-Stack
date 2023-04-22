package com.mr_kuro.crud_api.model;

import org.hibernate.annotations.SQLDelete;
import org.hibernate.annotations.Where;
import org.hibernate.validator.constraints.Length;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;

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

// @Getter
// @Setter
@Data // gera getters, setters, equalls hashcodes e tostrings
@Entity // classifica a classe como uma entidadae de um banco de dados
@Table(name = "Courses") // configurações referente a tabela que será criada no BD

//configurando o sql delete para um update de Course.Status
@SQLDelete(sql = "UPDATE Course SET Status = 'Inativo' WHERE id= ?") 
@Where(clause = "Status = 'Ativo'")
public class Course {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO) // gera automaticamente um valor de id autoincrement
    @JsonProperty("_id") // nome que será utilizado na converção para json
    // @JsonIgnore //ignora a propriedade ao converter em json
    private Long id;

    @NotNull
    @NotBlank
    @Length(min = 3, max = 200)
    @Column(name = "Name", length = 200, nullable = false) // configurações referente a coluna no BD
    private String name;

    @NotNull
    @NotBlank
    @Length(max = 10)
    @Pattern(regexp = "BackEnd|FrontEnd|FullStack")
    @Column(name = "Category", length = 10, nullable = false) // configurações referente a coluna no BD
    private String Category;

    @NotNull
    @Column(name = "Duration", length = 10, nullable = false) // configurações referente a coluna no BD
    private Long Duration;

    @NotNull
    @NotBlank
    @Length(max = 10)
    @Pattern(regexp = "Ativo|Inativo")
    @Column(name = "Status", length = 10, nullable = false) // configurações referente a coluna no BD
    private String Status = "Ativo";


}

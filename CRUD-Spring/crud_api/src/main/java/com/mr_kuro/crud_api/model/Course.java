package com.mr_kuro.crud_api.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

// @Getter
// @Setter
@Data // gera getters, setters, equalls hashcodes e tostrings 
@Entity // classifica a classe como uma entidadae de um banco de dados
@Table(name="Course") // configurações referente a tabela que será criada no BD
public class Course {
    
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO) // gera automaticamente um valor de id autoincrement
    @JsonProperty("_id") //nome que será utilizado na converção para json
    // @JsonIgnore //ignora a propriedade ao converter em json
    private Long id;

    @Column(name = "Name", length = 200, nullable = false) // configurações referente a coluna no BD
    private String name;

    @Column(name = "Category", length = 10, nullable = false) // configurações referente a coluna no BD
    private String Category;  
    
    @Column(name = "Duration", length = 10, nullable = false) // configurações referente a coluna no BD
    private Long Duration;
}

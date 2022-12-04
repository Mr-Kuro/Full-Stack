package com.mr_kuro.crud_api.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.mr_kuro.crud_api.model.Course;
import com.mr_kuro.crud_api.repository.CourseRepository;

import lombok.AllArgsConstructor;

@RestController //componente que permite expor a api e permitir o gêrenciamento pro spring
@RequestMapping("/api/courses") //pondto de acesso da api a partir do localhost
@AllArgsConstructor // gera automaticamente o construtor com os argumentos dos atributos
public class CurseController {

    private final CourseRepository courseRepository;
    
    // constructor feito a mão:
    /*public CurseController(CourseRepository courseRepository) {
        this.courseRepository = courseRepository;
    }*/

    // @RequestMapping(method = RequestMethod.GET)
    @GetMapping
    public List<Course> List() {
        return courseRepository.findAll();
    }
}

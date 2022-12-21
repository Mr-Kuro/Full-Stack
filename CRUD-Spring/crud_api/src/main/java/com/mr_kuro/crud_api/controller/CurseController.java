package com.mr_kuro.crud_api.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.mr_kuro.crud_api.model.Course;
import com.mr_kuro.crud_api.repository.CourseRepository;

import lombok.AllArgsConstructor;

@RestController // componente que permite expor a api e permitir o gêrenciamento pro spring
@RequestMapping("/api/courses") // pondto de acesso da api a partir do localhost
@AllArgsConstructor // gera automaticamente o construtor com os argumentos dos atributos
public class CurseController {

    private final CourseRepository courseRepository;

    /**
     * constructor feito a mão:
     * code: public CurseController(CourseRepository courseRepository) {
     * this.courseRepository = courseRepository;
     * }
     **/

    // @RequestMapping(method = RequestMethod.GET) pegando envios do bd
    @GetMapping
    public List<Course> List() {
        return courseRepository.findAll();
    }

    @GetMapping("/{id}") // adiciona uma variável a url
    public ResponseEntity<Course> FindById(@PathVariable("id") Long identificador ){ 
        //@PathVariable: diz ao spring para pegar a variavel passada na url
        return courseRepository.findById(identificador)
        .map(record -> ResponseEntity.ok().body(record))
        .orElse(ResponseEntity.notFound().build());
    }

    // @RequestMapping(method = RequestMethod.POST) // pegando envios do frontend
    @PostMapping
    // @ResponseStatus(code = HttpStatus.CREATED) // enviando resposta 201 ao
    // servidor
    public ResponseEntity<Course> Creat(@RequestBody Course course) {
        // System.out.println(course.getName()); // testando se a resposta está correta
        // return this.courseRepository.save(course); // usar com "@ResponseStatus"

        return ResponseEntity.status(HttpStatus.CREATED).body(this.courseRepository.save(course));

    }
}

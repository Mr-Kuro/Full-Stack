package com.mr_kuro.crud_api.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.mr_kuro.crud_api.model.Course;

@Repository // componente que diz ao spring que a classe faz uma conexão com o BD 
public interface CourseRepository extends JpaRepository<Course, Long>{

    
}

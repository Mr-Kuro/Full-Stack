package com.mr_kuro.crud_api;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.mr_kuro.crud_api.model.Course;
import com.mr_kuro.crud_api.repository.CourseRepository;

@SpringBootApplication
public class CrudApiApplication {

	public static void main(String[] args) {
		SpringApplication.run(CrudApiApplication.class, args);	
	}

	@Bean
	CommandLineRunner initDatabase(CourseRepository courseRepository){
		return args -> {
		Course c = new Course();
		c.setName("Angular + Spring");
		c.setCategory("FullStack");
		c.setDuration(4555L);

		// Course a = new Course();
		// a.setName("Angular");
		// a.setCategory("FrontEnd");
		// a.setDuration(2555L);
			
		// Course b = new Course();
		// b.setName("Spring");
		// b.setCategory("BackEnd");
		// b.setDuration(2555L);

		courseRepository.save(c);
		// courseRepository.save(a);
		// courseRepository.save(b);
		};
	}

}

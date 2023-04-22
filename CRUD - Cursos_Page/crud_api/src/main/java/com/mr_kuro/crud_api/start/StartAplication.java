package com.mr_kuro.crud_api.start;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.mr_kuro.crud_api.model.User;
import com.mr_kuro.crud_api.repository.UserRepository;
import org.springframework.web.bind.annotation.RestController;

@Component
public class StartAplication implements CommandLineRunner{

    @Autowired
    private UserRepository userRepository;

    @Override
    public void run(String... args) throws Exception {
        User user;

        user = userRepository.findByUsername("admin");
        System.out.println("\n\n\nuser = " + user +"\n\n\n");

        if (user == null){
            user = new User();
            user.setNome("ADMIN");
            user.setUsername("admin");
            user.setSenha("1234");
            user.setClasse("Manager");
            userRepository.save(user);
            System.out.println("\n\n\n\nuser = " + user +"\n\n\n\n");

        }

        user = userRepository.findByUsername("user");
        System.out.println("\n\n\n\nuser = " + user +"\n\n\n\n");

        if (user == null){
            user = new User();
            user.setNome("USER");
            user.setUsername("user");
            user.setSenha("1234");
            user.setClasse("Usuario");
            userRepository.save(user);
            System.out.println("\n\n\n\nuser = " + user +"\n\n\n\n");
        }
    }        
    
}

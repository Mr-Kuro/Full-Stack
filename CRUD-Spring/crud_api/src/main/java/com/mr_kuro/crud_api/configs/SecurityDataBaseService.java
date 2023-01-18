package com.mr_kuro.crud_api.configs;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import com.mr_kuro.crud_api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.mr_kuro.crud_api.model.User;


/**
 * @SecurityDataBaseService: essa classe de retorno de usuário retorna um UserDetails para a configuuração.
 * Esse retornoo pode ser usado por exemplo na classe SecurityDataBaseService.
 * Lá seus dados serão utilizados para autenticação de usuarios.
 */
@Service // informa ao spring que é um serviço, ou seja, uma lógica de negócio
public class SecurityDataBaseService implements UserDetailsService{
    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

        User userEntity = userRepository.findByUsername(username);

        if(userEntity == null) throw new UsernameNotFoundException(username);

        List<GrantedAuthority> authorities = new ArrayList<>();
        authorities.add( new SimpleGrantedAuthority("Role_" + userEntity.getClasse()));

        UserDetails user = new org.springframework.security.core.userdetails.User(userEntity.getUsername(), userEntity.getSenha(), authorities);

        return user;
    }
}

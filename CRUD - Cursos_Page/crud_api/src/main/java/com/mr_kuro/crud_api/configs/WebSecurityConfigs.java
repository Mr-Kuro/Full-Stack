package com.mr_kuro.crud_api.configs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.util.AntPathMatcher;

import com.mr_kuro.crud_api.model.User;

@Configuration // define como um bean de mapeamento automático
@EnableWebSecurity // fornecerá configuração via HttpSecurity
@EnableMethodSecurity(prePostEnabled = true) // veja lin> https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html
public class WebSecurityConfigs {
    // see abaout this component spring on link> https://spring.io/blog/2022/02/21/spring-security-without-the-websecurityconfigureradapter

    @Autowired
    private SecurityDataBaseService securityService;

    @Autowired
    private void globalUSerDetails(AuthenticationManagerBuilder auth) throws Exception{
        auth.userDetailsService(securityService).passwordEncoder(NoOpPasswordEncoder.getInstance());
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception{
        http
        .authorizeHttpRequests((auth) -> auth
                .requestMatchers(HttpMethod.POST, "/api/courses/login").permitAll()
                .requestMatchers(HttpMethod.GET, "/api/courses/").permitAll()
                .requestMatchers(HttpMethod.GET, "/api/courses/{id}").hasAnyRole("Manager")
                .requestMatchers(HttpMethod.POST, "/api/courses/{id}").hasRole("Manager")
                .requestMatchers(HttpMethod.PUT, "/api/courses/{id}").hasRole("Manager")
                .requestMatchers(HttpMethod.DELETE, "/api/courses/{id}").hasRole("Manager")
                .anyRequest().authenticated())
                .httpBasic(Customizer.withDefaults());
        return http.build();
    } /* definindo locais de acesso para ca classe de usuário
        * @Link:https://docs.spring.io/spring-security/site/docs/current/api/org/springframework/security/config/annotation/web/builders/HttpSecurity.html#authorizeRequests%25%29
       */


//    @Bean
//    protected void configure(HttpSecurity http) throws Exception {
//        http.authorizeRequests()
//                .antMatchers(HttpMethod.POST, "login").permitAll()
//                .antMatchers(HttpMethod.GET, "/api/courses").hasAnyRole("Usuario", "Manager")
//                .antMatchers(HttpMethod.POST, "/api/courses/{id}").hasRole("Manager")
//                .antMatcher(HttpMethod.PUT, "/api/courses/{id}").hasRole("Manager")
//                .antMatcher(HttpMethod.DELETE, "/api/courses/{id}").hasRole("Manager")
//                .anyRequest().authenticated().and().httpBasic();
//    }

    
}

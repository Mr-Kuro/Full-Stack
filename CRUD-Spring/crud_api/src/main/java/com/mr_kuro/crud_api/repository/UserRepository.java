package com.mr_kuro.crud_api.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.mr_kuro.crud_api.model.User;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, Integer>{

    @Query(value = "SELECT * FROM Usuarios WHERE Username = :username", nativeQuery = true)
    User findByUsername(@Param("username") String username);

    // @Query(value = "SELECT * FROM api_spring_security.tab_user JOIN api_spring_security.tab_user_roule WHERE  username = :username", nativeQuery = true)
    // User findByUsername(@Param("username") String username);
}

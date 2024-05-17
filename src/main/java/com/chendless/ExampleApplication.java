package com.chendless;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@SpringBootApplication
@EnableMongoRepositories
public class ExampleApplication {
    public static void main(final String... args) {
        SpringApplication.run(ExampleApplication.class, args);
    }

}

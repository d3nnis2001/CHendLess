package com.chendless.controller;

import com.chendless.service.DataService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

@Controller
@RequestMapping("/api/data")
public class DataController {
    private final DataService service;
    public DataController(DataService service) {
        this.service = service;
    }
    @PostMapping("/sendimage")
    public ResponseEntity<?> uploadFile(@RequestParam("image") MultipartFile file) {
        if (file.isEmpty()) {
            return new ResponseEntity<>("Bitte wählen Sie eine Datei aus", HttpStatus.BAD_REQUEST);
        }
        System.out.println("Wir sind im Controller");
        return null;
    }
}

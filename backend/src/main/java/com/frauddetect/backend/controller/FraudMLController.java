package com.frauddetect.backend.controller;

import org.springframework.web.bind.annotation.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;

@RestController
@RequestMapping("/api/ml")
public class FraudMLController {

    @PostMapping("/predict")
    public Map<String, Object> predictFraud(@RequestBody String inputJson) {

        Map<String, Object> response = new HashMap<>();

        try {
            // Run Python script with the JSON input string
            ProcessBuilder pb = new ProcessBuilder(
                    "C:\\Users\\vinay\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
                    "predict.py",
                    inputJson
            );

            // Folder where predict.py + model files exist
            pb.directory(new File("C:\\Users\\vinay\\Downloads\\PROJECT\\fraud-detection-blockchain\\backend\\mlmodel"));
            pb.redirectErrorStream(true);

            Process process = pb.start();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream())
            );

            StringBuilder output = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                output.append(line);
            }

            int exitCode = process.waitFor();

            // If Python script fails
            if (exitCode != 0) {
                response.put("error", "Python crashed");
                response.put("details", output.toString());
                return response;
            }

            // Convert Python output (JSON) -> Java Map
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(output.toString(), Map.class);

        } catch (Exception e) {
            response.put("exception", e.getMessage());
            return response;
        }
    }
}

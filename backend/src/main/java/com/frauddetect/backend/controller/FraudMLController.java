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
@CrossOrigin(origins = "*")
public class FraudMLController {

    @PostMapping("/predict")
    public Map<String, Object> predictFraud(@RequestBody String inputJson) {

        Map<String, Object> response = new HashMap<>();

        try {
            // Determine python executable path dynamically
            String pythonExec = System.getenv("PYTHON_PATH");
            if (pythonExec == null || pythonExec.trim().isEmpty()) {
                String osName = System.getProperty("os.name").toLowerCase();
                pythonExec = osName.contains("win") ? "python" : "python3";
            }

            // Determine ML directory path
            File mlDir = new File("mlmodel");
            if (!mlDir.exists()) {
                mlDir = new File("backend/mlmodel");
            }
            if (!mlDir.exists()) {
                mlDir = new File(".");
            }

            ProcessBuilder pb = new ProcessBuilder(
                    pythonExec,
                    "predict.py",
                    inputJson
            );

            pb.directory(mlDir);
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
                response.put("error", "Python execution failed with exit code " + exitCode);
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
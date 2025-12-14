package com.frauddetect.backend.blockchain;

import java.time.LocalDateTime;
import java.security.MessageDigest;

public class Block {

    public int index;
    public String timestamp;
    public String data;
    public String previousHash;
    public String hash;

    public Block(int index, String data, String previousHash) {
        this.index = index;
        this.timestamp = LocalDateTime.now().toString();
        this.data = data;
        this.previousHash = previousHash;
        this.hash = calculateHash();
    }

    public String calculateHash() {
        try {
            String input = index + timestamp + data + previousHash;
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(input.getBytes("UTF-8"));

            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                hexString.append(String.format("%02x", b));
            }
            return hexString.toString();

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}

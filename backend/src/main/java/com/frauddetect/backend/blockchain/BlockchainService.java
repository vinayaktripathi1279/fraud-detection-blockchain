package com.frauddetect.backend.blockchain;

import org.springframework.stereotype.Service;

@Service
public class BlockchainService {

    // Single blockchain instance shared across the app
    private final Blockchain blockchain = new Blockchain();

    // Add data to blockchain
    public void addRecord(String data) {
        blockchain.addBlock(data);
    }

    // Get full blockchain
    public Blockchain getBlockchain() {
        return blockchain;
    }
}

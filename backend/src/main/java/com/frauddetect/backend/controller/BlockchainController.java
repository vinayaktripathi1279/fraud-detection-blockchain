package com.frauddetect.backend.controller;

import com.frauddetect.backend.blockchain.Block;
import com.frauddetect.backend.blockchain.BlockchainService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/blockchain")
public class BlockchainController {

    private final BlockchainService blockchainService;

    // Constructor Injection (BEST PRACTICE)
    public BlockchainController(BlockchainService blockchainService) {
        this.blockchainService = blockchainService;
    }

    // Get full blockchain
    @GetMapping("/chain")
    public Object getChain() {
        return blockchainService.getBlockchain().getChain();
    }

    // Add a block manually
    @PostMapping("/add")
    public Block addBlock(@RequestBody String data) {
        blockchainService.addRecord(data);
        return blockchainService.getBlockchain().getLatestBlock();
    }
}

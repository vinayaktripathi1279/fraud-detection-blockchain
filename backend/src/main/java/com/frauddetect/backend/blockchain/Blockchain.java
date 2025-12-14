package com.frauddetect.backend.blockchain;

import java.util.ArrayList;
import java.util.List;

public class Blockchain {

    public List<Block> chain = new ArrayList<>();

    public Blockchain() {
        chain.add(createGenesisBlock());
    }

    private Block createGenesisBlock() {
        return new Block(0, "Genesis Block", "0");
    }

    public Block getLatestBlock() {
        return chain.get(chain.size() - 1);
    }

    public Block addBlock(String data) {
        Block newBlock = new Block(
                chain.size(),
                data,
                getLatestBlock().hash
        );
        chain.add(newBlock);
        return newBlock;
    }

    public List<Block> getChain() {
        return chain;
    }
}

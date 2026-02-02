package com.example;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.plugin.java.JavaPlugin;

/**
 * Main plugin class for ExamplePlugin.
 * 
 * This is a template - customize it for your plugin's needs.
 */
public class ExamplePlugin extends JavaPlugin {

    @Override
    public void onEnable() {
        // Save default config if it doesn't exist
        saveDefaultConfig();
        
        // Register event listeners
        // getServer().getPluginManager().registerEvents(new YourListener(), this);
        
        // Register commands
        // getCommand("example").setExecutor(new YourCommand());
        
        getLogger().info("ExamplePlugin has been enabled!");
    }

    @Override
    public void onDisable() {
        getLogger().info("ExamplePlugin has been disabled!");
    }
}

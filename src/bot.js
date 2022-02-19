require('dotenv').config();

const { Client } = require('discord.js');

const client = new Client();

console.log(process.env.DISCORD_JS_BOT_TOKEN);

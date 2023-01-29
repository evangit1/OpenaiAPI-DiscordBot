# OpenAI API interaction Bot

A simple Discord bot that interacts with OpenAI's API.
</p>Also comes with a daily limit for each discord user, so they don't spam it and rack up API cost.

<h1>Installation</h1><ol><li>Install the required packages: <code>discord</code>, <code>openai</code>, and <code>codeop</code> using pip by running the following command in your command prompt or terminal:</li></ol><pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install discord openai codeop</p>pip install discord.py</p>pip install openai
</p>pip install asyncio</p>python -m venv myenv</p>
</code></div></div></pre><ol start="2"><li><p>Add the following environment variables:</p><ul><li><code>openai_key</code>: Your OpenAI API key</li><li><code>bot_key</code>: Your Discord bot key</li></ul></li><li><p>Replace <code>openai key</code> and <code>bot key</code> in the code with the corresponding environment variables.</p></li><li><p>Run the code by executing the following command in your command prompt or terminal:</li></ol><pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">python OpenaiAPI-Disc-Bot.py</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-css"><span class="hljs-selector-tag"></span><span class="hljs-selector-class"></span>
</code></div></div></pre><p>Note: You also need to have a discord bot/OpenAI account and invite the bot to the server where you want to use it.</p></div>

# Commands

<code> I want: (Input) </code> Uses ada-001    <b>Doesn't produce great results, it's fast and doesn't cost much API usage</b> </p>
<code> I really want: (Input) </code> Uses davinci-003    <b>Produces great results, but it's slow and costs some API usage</b>

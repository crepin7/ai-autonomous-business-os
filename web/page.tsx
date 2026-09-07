export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white p-12">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-6xl font-bold mb-4">🚀 AI Autonomous Business OS</h1>
        <p className="text-2xl text-purple-200 mb-8">Launch a micro-SaaS in 24 hours. 6 AI agents. 0 employees.</p>
        <form className="bg-white/10 backdrop-blur p-8 rounded-2xl space-y-4">
          <input type="text" placeholder="Describe your business idea..." className="w-full p-4 rounded-lg bg-white/5 border border-white/20 text-white" />
          <input type="text" placeholder="Target market (e.g. lawyers, fitness coaches)" className="w-full p-4 rounded-lg bg-white/5 border border-white/20 text-white" />
          <button className="w-full bg-gradient-to-r from-pink-500 to-purple-600 p-4 rounded-lg font-bold text-lg">Launch My Business →</button>
        </form>
      </div>
    </main>
  );
}

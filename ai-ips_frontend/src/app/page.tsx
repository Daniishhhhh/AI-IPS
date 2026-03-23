"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";
import StatCard from "@/components/StatCard";
import EventTable from "@/components/EventTable";

type EventItem = {
  id: number;
  timestamp: string;
  attack_type: string;
  confidence: number;
  recommended_action: string;
  total_latency_ms: number;
};

export default function HomePage() {
  const [events, setEvents] = useState<EventItem[]>([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await api.get("/events/recent");
        setEvents(response.data);
      } catch (error) {
        console.error("Failed to load events:", error);
      }
    };

    fetchEvents();
  }, []);

  const totalEvents = events.length;
  const blockedEvents = events.filter((e) =>
    e.recommended_action.startsWith("BLOCK")
  ).length;
  const benignEvents = events.filter((e) => e.attack_type === "BENIGN").length;
  const latestAttack = events.length > 0 ? events[0].attack_type : "N/A";

  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-[1400px]">
        <h1 className="mb-2 text-4xl font-bold text-gray-900">AI-IPS Dashboard</h1>
        <p className="mb-8 text-gray-600">
          AI-powered intrusion detection and security event monitoring
        </p>

        <div className="mb-8 grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
          <StatCard title="Recent Events Loaded" value={totalEvents} />
          <StatCard title="Blocked Events" value={blockedEvents} />
          <StatCard title="Benign Events" value={benignEvents} />
          <StatCard title="Latest Attack Type" value={latestAttack} />
        </div>

        <div className="mb-4 flex gap-4">
          <a
            href="/predict"
            className="rounded-xl bg-black px-5 py-3 text-white"
          >
            Go to Predict Page
          </a>
          <a
            href="/logs"
            className="rounded-xl border border-black px-5 py-3 text-black"
          >
            View All Logs
          </a>
        </div>

        <h2 className="mb-4 text-2xl font-semibold text-gray-900">Recent Security Events</h2>
        <EventTable events={events} />
      </div>
    </main>
  );
}
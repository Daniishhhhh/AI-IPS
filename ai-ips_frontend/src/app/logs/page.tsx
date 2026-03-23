"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";
import EventTable from "@/components/EventTable";

type EventItem = {
  id: number;
  timestamp: string;
  attack_type: string;
  confidence: number;
  recommended_action: string;
  total_latency_ms: number;
};

export default function LogsPage() {
  const [events, setEvents] = useState<EventItem[]>([]);

  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const response = await api.get("/events?limit=100");
        setEvents(response.data);
      } catch (error) {
        console.error("Failed to load logs:", error);
      }
    };

    fetchLogs();
  }, []);

  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-[1400px]">
        <h1 className="mb-2 text-4xl font-bold text-gray-900">Security Event Logs</h1>
        <p className="mb-8 text-gray-600">
          Historical intrusion detection events from SQLite
        </p>

        <div className="mb-4 flex gap-4">
          <a
            href="/"
            className="rounded-xl border border-black px-5 py-3 text-black"
          >
            Dashboard
          </a>
          <a
            href="/predict"
            className="rounded-xl border border-black px-5 py-3 text-black"
          >
            Predict
          </a>
        </div>

        <EventTable events={events} />
      </div>
    </main>
  );
}
type EventItem = {
  id: number;
  timestamp: string;
  attack_type: string;
  confidence: number;
  recommended_action: string;
  total_latency_ms: number;
};

type EventTableProps = {
  events: EventItem[];
};

function getAttackBadgeClass(attackType: string) {
  switch (attackType) {
    case "BENIGN":
      return "bg-green-100 text-green-700";
    case "DDOS":
    case "DOS":
      return "bg-red-100 text-red-700";
    case "BOT":
      return "bg-purple-100 text-purple-700";
    case "BRUTEFORCE":
      return "bg-orange-100 text-orange-700";
    case "PORTSCAN":
      return "bg-yellow-100 text-yellow-700";
    case "INFILTRATION":
      return "bg-pink-100 text-pink-700";
    default:
      return "bg-gray-100 text-gray-700";
  }
}

function getActionBadgeClass(action: string) {
  if (action.startsWith("BLOCK")) return "bg-red-100 text-red-700";
  if (action === "ALLOW") return "bg-green-100 text-green-700";
  if (action.includes("MONITOR")) return "bg-yellow-100 text-yellow-700";
  if (action.includes("ISOLATE")) return "bg-purple-100 text-purple-700";
  if (action.includes("ESCALATE")) return "bg-pink-100 text-pink-700";
  return "bg-gray-100 text-gray-700";
}

function formatTimestamp(timestamp: string) {
  const utcDate = new Date(timestamp.replace(" ", "T") + "Z");

  return utcDate.toLocaleString("en-IN", {
    timeZone: "Asia/Kolkata",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  });
}

export default function EventTable({ events }: EventTableProps) {
  if (!events.length) {
    return (
      <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
        <p className="text-gray-500">No events found.</p>
      </div>
    );
  }

  return (
    <div className="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm">
      <div className="max-h-[500px] overflow-auto">
        <table className="min-w-full text-sm">
          <thead className="sticky top-0 bg-gray-100 text-left text-gray-800">
            <tr>
              <th className="px-4 py-3 font-semibold">ID</th>
              <th className="px-4 py-3 font-semibold">Timestamp</th>
              <th className="px-4 py-3 font-semibold">Attack Type</th>
              <th className="px-4 py-3 font-semibold">Confidence</th>
              <th className="px-4 py-3 font-semibold">Action</th>
              <th className="px-4 py-3 font-semibold">Latency (ms)</th>
            </tr>
          </thead>

          <tbody>
            {events.map((event) => (
              <tr
                key={event.id}
                className="border-t border-gray-100 hover:bg-gray-50"
              >
                <td className="px-4 py-3 text-gray-800">{event.id}</td>

                <td className="whitespace-nowrap px-4 py-3 text-gray-700">
                  {formatTimestamp(event.timestamp)}
                </td>

                <td className="px-4 py-3">
                  <span
                    className={`rounded-full px-3 py-1 text-xs font-semibold ${getAttackBadgeClass(
                      event.attack_type
                    )}`}
                  >
                    {event.attack_type}
                  </span>
                </td>

                <td className="px-4 py-3 font-medium text-gray-700">
                  {event.confidence.toFixed(4)}
                </td>

                <td className="px-4 py-3">
                  <span
                    className={`rounded-full px-3 py-1 text-xs font-semibold ${getActionBadgeClass(
                      event.recommended_action
                    )}`}
                  >
                    {event.recommended_action}
                  </span>
                </td>

                <td className="px-4 py-3 font-medium text-gray-700">
                  {event.total_latency_ms.toFixed(2)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
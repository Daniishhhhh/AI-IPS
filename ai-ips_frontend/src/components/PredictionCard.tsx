type PredictionResult = {
  attack_type: string;
  confidence: number;
  recommended_action: string;
  binary_latency_ms: number;
  multiclass_latency_ms: number;
  total_latency_ms: number;
};

type PredictionCardProps = {
  result: PredictionResult | null;
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

export default function PredictionCard({ result }: PredictionCardProps) {
  if (!result) return null;

  return (
    <div>
      <h2 className="mb-4 text-xl font-bold text-gray-900">Prediction Result</h2>

      <div className="space-y-4 rounded-xl bg-gray-50 p-5">
        <div>
          <p className="mb-2 text-sm text-gray-500">Attack Type</p>
          <span
            className={`rounded-full px-3 py-1 text-sm font-semibold ${getAttackBadgeClass(
              result.attack_type
            )}`}
          >
            {result.attack_type}
          </span>
        </div>

        <div>
          <p className="mb-1 text-sm text-gray-500">Confidence</p>
          <p className="text-lg font-semibold text-gray-900">
            {result.confidence.toFixed(4)}
          </p>
        </div>

        <div>
          <p className="mb-2 text-sm text-gray-500">Recommended Action</p>
          <span
            className={`rounded-full px-3 py-1 text-sm font-semibold ${getActionBadgeClass(
              result.recommended_action
            )}`}
          >
            {result.recommended_action}
          </span>
        </div>

        <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
          <div className="rounded-xl bg-white p-4 shadow-sm">
            <p className="text-sm text-gray-500">Binary Latency</p>
            <p className="text-lg font-bold text-gray-900">
              {result.binary_latency_ms} ms
            </p>
          </div>

          <div className="rounded-xl bg-white p-4 shadow-sm">
            <p className="text-sm text-gray-500">Multiclass Latency</p>
            <p className="text-lg font-bold text-gray-900">
              {result.multiclass_latency_ms} ms
            </p>
          </div>

          <div className="rounded-xl bg-white p-4 shadow-sm">
            <p className="text-sm text-gray-500">Total Latency</p>
            <p className="text-lg font-bold text-gray-900">
              {result.total_latency_ms} ms
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
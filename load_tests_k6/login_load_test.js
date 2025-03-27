import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 50,
  duration: '15s',
};

const userAgents = [
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
  'Mozilla/5.0 (X11; Linux x86_64)',
  'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)',
  'Mozilla/5.0 (Android 11; Mobile; rv:87.0)',
];

export default function () {
  const randomUserAgent = userAgents[Math.floor(Math.random() * userAgents.length)];

  http.get('https://www.saucedemo.com/', {
    headers: {
      'User-Agent': randomUserAgent,
    },
  });

  sleep(1);
}

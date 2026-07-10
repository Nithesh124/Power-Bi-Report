import React, { useMemo, useState } from 'react';

function InvoiceList({ invoices }) {
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = useMemo(
    () => invoices.filter(inv =>
      inv.clientName.toLowerCase().includes(searchTerm.toLowerCase())
    ),
    [invoices, searchTerm]
  );

  return (
    <>
      <input
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search by client name..."
      />
      <ul>
        {filtered.map(inv => (
          <li key={inv.id}>
            {inv.clientName} - ${inv.total}
          </li>
        ))}
      </ul>
    </>
  );
}

export default InvoiceList;
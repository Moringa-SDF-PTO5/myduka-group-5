/* eslint-disable react/prop-types */
import React from 'react'
import {Link} from 'react-router-dom'
import { sidebarNav } from './SidebarData'
import './css/Sidebar.css'

const Sidebar = ({role}) => {
  const allowedUserNav = sidebarNav.filter(sidebar => sidebar?.allowedRoles.includes(role))
  // console.log(allowedUserNav)
  return (
    <aside className='w-56 bg-zinc-900 border-r border-gray-100'>
      <header className='h-16 flex items-center justify-center'>
        <h1 className='text-lg text-zinc-50'>MyDuka</h1>
      </header>
      <ul className='space-y-2'>
        {allowedUserNav.map(sidebar => (
          <li key={sidebar.title} className='text-zinc-400 px-4 py-2 transition-colors hover:bg-zinc-800'>
           <Link className='w-full flex items-center gap-2' to={sidebar.link}>
           {sidebar.icon}
           <span>{sidebar.title}</span>
           </Link>
          </li>
        ))}
      </ul>
    </aside>
  )
}

export default Sidebar

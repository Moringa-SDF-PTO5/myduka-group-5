/* eslint-disable react/prop-types */
import React from 'react'
import { Link } from 'react-router-dom'
import { sidebarNav } from './SidebarData'

const Sidebar = ({ role }) => {
    const allowedUserNav = sidebarNav.filter((sidebar) =>
        sidebar?.allowedRoles.includes(role)
    )
    // console.log(allowedUserNav)
    return (
        <aside className='bg-gray-100 text-gray-900 h-screen px-4 w-16 md:w-64 border-r border-gray-300'>
            <header className='h-16 flex items-center justify-center'>
                <h1 className='text-2x1 font-bold hidden md:block'>MyDuka</h1>
            </header>
            <ul className='flex flex-col mt-5 text-l'>
                {allowedUserNav.map((sidebar) => (
                    <li
                        key={sidebar.title}
                        className='flex items-center py-5 px-2 space-x-4 hover:rounded hover:cursor-pointer hover:bg-gray-900 hover:text-white'
                    >
                        <Link
                            className='w-full flex items-center gap-3'
                            to={sidebar.link}
                        >
                            {sidebar.icon}
                            <span className='hidden md:inline'>
                                {sidebar.title}
                            </span>
                        </Link>
                    </li>
                ))}
            </ul>
        </aside>
    )
}

// return (
//   <aside className='w-56 bg-zinc-900 h-screen border-r border-gray-100'>
//     <header className='h-16 flex items-center justify-center'>
//       <h1 className='text-lg text-zinc-50'>MyDuka</h1>
//     </header>
//     <ul className='space-y-2'>
//       {allowedUserNav.map(sidebar => (
//         <li key={sidebar.title} className='text-zinc-400 px-6 py-4 transition-colors hover:bg-zinc-800'>
//          <Link className='w-full flex items-center gap-3' to={sidebar.link}>
//          {sidebar.icon}
//          <span>{sidebar.title}</span>
//          </Link>
//         </li>
//       ))}
//     </ul>
//   </aside>
// )
// }

// bg-gray-100 text-gray-900 h-screen px-4 fixed w-16 md:w-64 border-r border-gray-300
// w-56 bg-zinc-900 h-screen border-r border-gray-100

export default Sidebar

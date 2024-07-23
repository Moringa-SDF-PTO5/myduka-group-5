import React from 'react'
import {Outlet} from 'react-router-dom'
import {useSelector} from 'react-redux'
import Sidebar from './Sidebar.jsx'

export default function Layout(){
    const state = useSelector(state => state.user);

    return <div className='h-screen flex'>
        <Sidebar role={state.user.role}/>
        <main className='flex-1 flex flex-col'>
            <header className='h-16 border-b border-slate-100'>
                header
            </header>
            <main className='flex-1 px-8 py-4'>
                <Outlet />
            </main>
        </main>
    </div>
}